import time

from osv import fields, osv

class obj1(osv.osv):
    _name = 'ex1.obj1'
    _description = 'ex1.obj1'

    def _get_x_name(self, cr, uid, ids, arg1, arg2, context):
        result = {}
        for obj1 in self.browse(cr, uid, ids):
            result[obj1.id] = obj1.name
        return result

    def _get_y_name(self, cr, uid, ids, arg1, arg2, context):
        result = {}
        for obj1 in self.browse(cr, uid, ids):
            result[obj1.id] = obj1.name
        return result

    _columns = {
        'name': fields.char('Name', size=50, translate=True, select=1),
        'x_name': fields.function(_get_x_name, method=True, type='char', string='x_name', store=True),
        'y_name': fields.function(_get_y_name, method=True, type='char', string='y_name'),
        'odate': fields.datetime('Date'),
        'ointeger': fields.integer('Integer'),
        'ofloat': fields.float('Float'),
        'oboolean': fields.boolean('Boolean'),
        'otext': fields.text('Text', help="No limit size"),
        'obj2_ids': fields.many2one('ex1.obj2', 'Obj2', help="help ob2"),
        'company_id': fields.many2one('res.company'),
    }

    _defaults = {
        'odate': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'), 
    }

    def mybutton(self, cr, uid, ids, context=None):
        print 'test my button'
        return True

obj1()

class obj2(osv.osv):
    _name = 'ex1.obj2'
    _description = 'ex1.obj2'

    _columns = {
        'name': fields.char('name', size=50, required=True),
        'choice': fields.selection([('yes', 'Yes'), ('no', 'No')], 'yes/no'),
    }

obj2()

class obj3(osv.osv):
    _name = 'ex1.obj3'
    _description = 'ex1.obj3'

    _columns = {
        'name': fields.char('name', size=50, required=True),
        'obj2_ids': fields.many2many('ex1.obj2', 'ex1_obj2_3_rel', 'obj3_id', 'obj2_id', 'Obj3 & Obj2'),
    }

obj3()

class obj4(osv.osv):
    _name = 'ex1.obj4'
    _description = 'ex1.obj4'

    _columns = {
        'name': fields.char('name', size=50, required=True),
        'obj4_lines': fields.one2many('ex1.obj4.line', 'obj4_id', 'Obj4 Lines'),
    }

obj4()

class obj4_line(osv.osv):
    _name = 'ex1.obj4.line'
    _description = 'ex1.obj4.line'

    _columns = {
        'obj4_id': fields.many2one('ex1.obj4', 'Obj4'),
        'name': fields.char('name', size=50, required=True),
        'ointeger': fields.integer('Integer'),
        'ofloat': fields.float('Float'),
    }

obj4()

class obj5(osv.osv):
    _name = 'ex1.obj5'

obj5()
