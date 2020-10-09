from sampleapp import myapp

@myapp.route('/')
def helloworld():
    return 'Hello World!'

@myapp.route('/peru')
def helloperu():
    return 'Imaynallam Peru...!'
