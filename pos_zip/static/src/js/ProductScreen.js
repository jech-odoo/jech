odoo.define('pos_zip.ProductScreen', function(require) {
    'use strict';


const ProductScreen = require('point_of_sale.ProductScreen');
const Registries = require('point_of_sale.Registries');
const { useListener } = require('web.custom_hooks');

 
const PosSaleProductScreen = (ProductScreen) =>
  class extends ProductScreen
  {
    constructor() {
        super(...arguments);
        useListener('click-customer', this._onClickCustomer);
        useListener('click-pay', this._onClickPay);
    }


    async _onClickPay() {
        var self = this;
        const currentClient = this.currentOrder.get_client();
        if(currentClient && !currentClient.zip) {
            
            const { confirmed, payload} = await this.showPopup('TextInputPopup', {
                title: this.env._t('Text Area Popup'),
                body: this.env._t('This click is successfully done.'),
                
            });
      
            if (confirmed) {
                console.log(payload, 'payload')
                currentClient.zip = await this.rpc({
                    model: 'res.partner',
                    method: 'write',
                    args: [[currentClient.id], { zip: payload }],
                    
                }).then(function (e) {
                     self.env.pos.load_new_partners();
                     self.currentOrder.get_client();
                });
              
            }
       
          }
          else{ return this.showScreen('PaymentScreen');}
       
    }
 };

 Registries.Component.extend(ProductScreen,PosSaleProductScreen);

 return ProductScreen;
});
