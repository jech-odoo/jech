    odoo.define('point_of_sale_payment.ProductScreen', function(require) {
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
            const currentClient = this.currentOrder.get_client();
            if (currentClient) {
                return this.showScreen('PaymentScreen');
            }else{
            this.showPopup('ErrorPopup', {
                title: this.env._t('Error'),
                body: this.env._t('Not select customer,so please select customer.'),
            });

        }
    }
     };

     Registries.Component.extend(ProductScreen,PosSaleProductScreen);

     return ProductScreen;
});
