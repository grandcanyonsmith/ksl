from flask import Flask, render_template, request, redirect, url_for
from flask_script import Manager, Command, Shell
from forms import ItemInsertForm
from forms import ItemRemoveForm
import pandas as pd
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'

@app.route('/insert/', methods=['get', 'post'])

def insert():
    form = ItemInsertForm()
    if form.validate_on_submit():

        df = pd.read_csv('keywords.csv')
        
        item_name = form.item_name.data
        minimum = form.minimum.data
        maximum = form.maximum.data
        print(item_name)
        print(minimum)
        print(maximum)
        print("\nData received. Now redirecting ...")
        
        found = df[df['Item'].str.contains(item_name)]
        isFound = found['Item'].count()
        print(isFound)

        if(isFound==0):
            print ("Unique Item Name")
            new_item = {'Item':item_name, 'Minimum': minimum, 'Maximum': maximum}
            print (new_item)
            new_df = df
            new_df = new_df.append(new_item, ignore_index=True)
            new_df.reset_index(drop=True, inplace=True)
            new_df.to_csv('keywords.csv', index=False)
            print ("Successfully inserted Item - ", item_name)
        else:
            print ("Duplicate Item")
            
        return redirect(url_for('insert'))
    return render_template('item.html', form=form)

@app.route('/delete/', methods=['get', 'post'])
def delete():
    form = ItemRemoveForm()
    if form.validate_on_submit():

        df = pd.read_csv('keywords.csv')
        
        item_name = form.remove_item_name.data
        
        print(item_name)
        
        print("\nData received. Now Searching for removal ...")
        
        found = df[df['Item'].str.contains(item_name)]
        isFound = found['Item'].count()
        print(isFound)

        if(isFound!=0):
            print ("Item found")
            new_df = df
            new_df = new_df[new_df.Item != item_name]
            new_df.reset_index(drop=True, inplace=True)
            new_df.to_csv('keywords.csv', index=False)
            print ("Successfully Deleted Item - ", item_name)
        else:
            print ("Not found")
            
        return redirect(url_for('delete'))

    return render_template('item.html', form=form)
@app.route('/')
def hello_world():
    return render_template('main.html')
if __name__ == "__main__":
    app.run(debug = True)

