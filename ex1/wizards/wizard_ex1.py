from osv import osv, fields

class wizard_ex1(osv.osv_memory):
    _name = 'wizard.ex1'
    _columns = {
            'name': fields.char('Name', size=50),

    }

    def mybutton1(self, cr, uid, ids, context=None):
        print 'test my button'
        return True

    def mybutton2(self, cr, uid, ids, context=None):
        print 'test my button'
        return True

wizard_ex1()
