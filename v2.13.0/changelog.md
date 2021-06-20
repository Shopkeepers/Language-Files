# Changelog v2.13.0

The default english language file is now called `en-default`.

### New messages:
* Various messages were moved from settings in the config into the language file:
  * `editor-title`
  * `for-hire-title`
  * `nameplate-prefix`: Also changed the color to a dark green.
  * `sign-shop-first-line`: This has been replaced with 8 new messages for the sign lines of different types of shops.
    * `admin-sign-shop-line1/2/3/4`
    * `player-sign-shop-line1/2/3/4`
    * The appearance of sign shops has also changed: They are slightly more colorful now.
* `must-target-container`
* `no-player-shops-via-command`
* `button-name-villager`
* `button-name-villager-lore`
* `type-new-villager-name`
* `villager-name-set`
* `villager-name-invalid`
* `button-snowman-pumpkin-head`
* `button-snowman-pumpkin-head-lore`
* `button-shulker-color`
* `button-shulker-color-lore`
* `button-invulnerability`
* `button-invulnerability-lore`
* `shops-already-removed`
* `shop-removals-cancelled`
* `shop-removed`
* `shop-already-removed`
* `shop-removal-cancelled`
* `confirm-remove-shop`
* `command-description-remove`
* `cannot-trade-unexpected-trade`
* `cannot-trade-items-not-strictly-matching`
* `cannot-trade-insufficient-storage-space`
* `cannot-trade-insufficient-currency`
* `cannot-trade-insufficient-stock`
* `cannot-trade-insufficient-writable-books`
* `trade-notification-one-item`
* `trade-notification-two-items`
* `buy-notification-one-item`
* `buy-notification-two-items`
* `trade-notification-player-shop`
* `trade-notification-named-player-shop`
* `trade-notification-admin-shop`
* `trade-notification-named-admin-shop`
* `trade-notification-trade-count`
* `owner-trade-notification-one-item`
* `owner-trade-notification-two-items`
* `owner-buy-notification-one-item`
* `owner-buy-notification-two-items`
* `owner-trade-notification-shop`
* `owner-trade-notification-named-shop`
* `owner-buy-notification-shop`
* `owner-buy-notification-named-shop`
* `owner-trade-notification-trade-count`
* `state-enabled`
* `state-disabled`
* `button-trade-notifications`
* `button-trade-notifications-lore`
* `confirmation-ui-delete-shop-title`
* `confirmation-ui-delete-shop-confirm-lore`
* `confirmation-ui-confirm`
* `confirmation-ui-cancel`
* `confirmation-ui-cancel-lore`
* `confirmation-ui-aborted`
* `villager-no-longer-exists`
* `confirmation-ui-delete-villager-title`
* `confirmation-ui-delete-villager-confirm-lore`
* `villager-removed`
* `button-sign-glowing-text`
* `button-sign-glowing-text-lore`
* `button-axolotl-variant`
* `button-axolotl-variant-lore`
* `button-glow-squid-dark`
* `button-glow-squid-dark-lore`
* `button-goat-screaming`
* `button-goat-screaming-lore`

### Changed messages:
* All message keys were changed to no longer start with the `msg` prefix.
* `cant-hire`: Renamed to `cannot-hire`
* `cant-hire-shop-type`: Renamed to `cannot-hire-shop-type`
* `cant-trade-with-own-shop`: Renamed to `cannot-trade-with-own-shop`
* `cant-trade-while-owner-online`: Renamed to `cannot-trade-while-owner-online`
* `cant-trade-with-shop-missing-container`: Renamed to `cannot-trade-with-shop-missing-container`
* `villager-editor-title`: Changed the default color of to be less bright.
* `too-many-shops`: Changed the message to be more general.
* `creation-item-selected`: Changed to clarify that one has to not aim at any block in order to select the shop or object type.
* `command-description-remove`: Renamed to `command-description-remove-all` and slightly changed.
* `command-description-list`
* `removed-admin-shops`: Renamed to `admin-shops-removed` and slightly changed.
* `Rremoved-shops-of-player`: Renamed to `shops-of-player-removed` and slightly changed.
* `removed-player-shops`: Renamed to `shops-of-player-removed` and slightly changed.
* `owner-set`
* `set-for-hire`
* `confirm-remove-all-admin-shops`
* `confirm-remove-all-own-shops`
* `confirm-remove-all-shops-of-player`
* `confirm-remove-all-player-shops`

### Removed messages:
* `no-admin-shop-type-selected`
* `no-player-shop-type-selected`
