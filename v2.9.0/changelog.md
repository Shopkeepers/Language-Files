# Changelog v2.9.0

### New messages:

* msg-command-argument-requires-player
* msg-ambiguous-player-name
* msg-ambiguous-player-name-entry
* msg-ambiguous-player-name-more

### Changed messages:

* msg-list-shops-entry: 'object type' changed to 'object', and the arguments '{shopSessionId}' and '{shopId}' changed to '{shopId}' and '{shopUUID}' respectively. Argument '{shopSessionId}' still works but will likely get removed in the future.
* msg-villager-for-hire: The german translation was slightly changed.
* Normalized the representation of various multi-line messages inside the default config:
  * msg-creation-item-selected
  * msg-shop-setup-desc-selling
  * msg-shop-setup-desc-buying
  * msg-shop-setup-desc-trading
  * msg-shop-setup-desc-book
  * msg-shop-setup-desc-admin-regular
* Added {shopsCount} argument to shop removal confirmation messages:
  * msg-confirm-remove-admin-shops
  * msg-confirm-remove-own-shops
  * msg-confirm-remove-player-shops
  * msg-confirm-remove-all-player-shops

### Removed messages:

* The default german translation contained a few no longer used messages: msg-button-type and msg-button-type-lore
