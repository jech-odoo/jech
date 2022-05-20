odoo.define('project.template', function(require) {
    "use strict";

    var KanbanController = require('web.KanbanController');
    var KanbanView = require('web.KanbanView');

    var viewRegistry = require('web.view_registry');

    function renderTemplateButton() {
        if (this.$buttons) {
            var self = this;
            this.$buttons.on('click', '.o_button_create_template', function() {
                self.do_action({
                    name: 'Create a Project',
                    type: 'ir.actions.act_window',
                    res_model: 'project.template.wizard',
                    target: 'new',
                    views: [
                        [false, 'form']
                    ],
                });
            });
        }
    }

    var ProjectKanbanController = KanbanController.extend({
        willStart: function() {
            var self = this;
            self.buttons_template = 'ProjectTemplateKanbanView.buttons';
            return Promise.all([this._super.apply(this, arguments)]);
        },
        renderButtons: function() {
            this._super.apply(this, arguments);
            renderTemplateButton.apply(this, arguments);
        }
    });

    var ProjectTemplateKanbanView = KanbanView.extend({
        config: _.extend({}, KanbanView.prototype.config, {
            Controller: ProjectKanbanController,
        }),
    });

    viewRegistry.add('project_template_kanban', ProjectTemplateKanbanView);
});