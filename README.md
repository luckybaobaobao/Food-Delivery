# food-products

There are Two files:

Assigment is the first backend test.

And assignmentelasticsearch is the second elastic search test.

First Assigment to test it, you need run test.

Second Assignment, you need to install all requirments in file requirments.

And there are tow files. 

One is importer:

At begining you have to run elasticsearch on your local - bin/elasticsearch.

To create an index, you need to set Enviroment parameter : MATHEM_PRODUCTS_URL (The url you offered)

And then run main.py and you will got and index product. You could you kibana to have a look.

After you got the index:

You can open another file called search, in search you need to set several parameters also.

FLASK_APP = search, FLASK_ENV = development, LOGLEVEL = debug

And then start the app.

You can fetch this three endpoints "/most-expensive", "/greenest", "/all-week-long" on your local.
