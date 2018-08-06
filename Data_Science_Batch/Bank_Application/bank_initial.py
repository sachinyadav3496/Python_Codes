import json
data = { 
        'user' : [ 'ram','john','harry' ] , 
        'acc' : [ 1001, 1002, 1003 ] , 
        'password'   :[ 'abcdef','hey@123','redhat@asimov' ],
        'bal' : [ 25000.0,1500.0,16644.0 ] , 
}

f = open('bank.db','w')
json.dump(data,f)
f.close()
