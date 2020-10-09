from sampleapp import myapp

@myapp.route('/')
def helloworld():
    return 'Hello World!'

@myapp.route('/peru')
def helloworld():
    return 'Imaynallam Peru...!'
