# Changelog

## v2.19.0

### New messages

* Added `traded-command-set`.
* Added `traded-command-removed`.
* Added `traded-command-view`.
* Added `traded-command-view-unset`.
* Added `command-description-settradedcommand`.
* Added `no-shops-found`.
* Added `confirm-replace-all-shops-with-vanilla-villagers`.
* Added `all-shops-replaced-with-vanilla-villagers`.
* Added `command-description-replace-all-with-vanilla-villagers`.

## v2.17.0

### New messages

* Added `shop-object-type-hanging-sign`. Existing translations were adjusted.

## v2.16.0

### New messages

* Added `button-move`.
* Added `button-move-lore`.
* Added `click-new-shop-location`.
* Added `shopkeeper-moved`.
* Added `shopkeeper-move-aborted`.
* Added `button-frog-variant`.
* Added `button-frog-variant-lore`.
* Added `button-goat-left-horn`.
* Added `button-goat-left-horn-lore`.
* Added `button-goat-right-horn`.
* Added `button-goat-right-horn-lore`.

### Changed messages

* Changed `mob-cannot-spawn-on-peaceful-difficulty`.
* Changed `restricted-area`.

## v2.15.0

### New messages

* Added `button-horse-saddle`.
* Added `button-horse-saddle-lore`.
* Added `must-target-block`.
* Added `missing-spawn-location`.
* Added `spawn-block-not-empty`.
* Added `invalid-spawn-block-face`.
* Added `mob-cannot-spawn-on-peaceful-difficulty`.
* Added `restricted-area`.
* Added `location-already-in-use`.
* Added `must-hold-item-in-main-hand`.
* Added `currency-item-set-to-main-hand-item`.
* Added `command-description-set-currency`.
* Added `selling-shop.empty-trade.result-item`.
* Added `selling-shop.empty-trade.result-item-lore`.
* Added `selling-shop.empty-trade.item1`.
* Added `selling-shop.empty-trade.item1-lore`.
* Added `selling-shop.empty-trade.item2`.
* Added `selling-shop.empty-trade.item2-lore`.
* Added `selling-shop.empty-item1`.
* Added `selling-shop.empty-item1-lore`.
* Added `selling-shop.empty-item2`.
* Added `selling-shop.empty-item2-lore`.
* Added `buying-shop.empty-trade.result-item`.
* Added `buying-shop.empty-trade.result-item-lore`.
* Added `buying-shop.empty-trade.item1`.
* Added `buying-shop.empty-trade.item1-lore`.
* Added `buying-shop.empty-result-item`.
* Added `buying-shop.empty-result-item-lore`.
* Added `trading-shop.empty-trade.result-item`.
* Added `trading-shop.empty-trade.result-item-lore`.
* Added `trading-shop.empty-trade.item1`.
* Added `trading-shop.empty-trade.item1-lore`.
* Added `trading-shop.empty-trade.item2`.
* Added `trading-shop.empty-trade.item2-lore`.
* Added `trading-shop.empty-result-item`.
* Added `trading-shop.empty-result-item-lore`.
* Added `trading-shop.empty-item1`.
* Added `trading-shop.empty-item1-lore`.
* Added `trading-shop.empty-item2`.
* Added `trading-shop.empty-item2-lore`.
* Added `book-shop.empty-trade.result-item`.
* Added `book-shop.empty-trade.result-item-lore`.
* Added `book-shop.empty-trade.item1`.
* Added `book-shop.empty-trade.item1-lore`.
* Added `book-shop.empty-trade.item2`.
* Added `book-shop.empty-trade.item2-lore`.
* Added `book-shop.empty-item1`.
* Added `book-shop.empty-item1-lore`.
* Added `book-shop.empty-item2`.
* Added `book-shop.empty-item2-lore`.
* Added `unknown-currency`.

### Changed messages

* Slightly changed the default `must-target-container` message.
* Changed `invalid-snapshot-id`.
* Changed `invalid-snapshot-name`.
* Changed `currency-items-given`.
* Changed `currency-items-received`.

### Removed messages

* Removed `shop-create-fail`.
* Removed `high-currency-items-given`.
* Removed `high-currency-items-received`.
* Removed `high-currency-disabled`.

## v2.14.0

### New messages

* `button-tropical-fish-pattern`
* `button-tropical-fish-pattern-lore`
* `button-tropical-fish-body-color`
* `button-tropical-fish-body-color-lore`
* `button-tropical-fish-pattern-color`
* `button-tropical-fish-pattern-color-lore`
* `button-puffer-fish-puff-state`
* `button-puffer-fish-puff-state-lore`
* `date-time-format`
* `shop-no-longer-exists`
* `snapshot-list-header`
* `snapshot-list-entry`
* `invalid-snapshot-id`
* `invalid-snapshot-name`
* `snapshot-name-too-long`
* `snapshot-name-invalid`
* `snapshot-name-already-exists`
* `snapshot-created`
* `confirm-remove-snapshot`
* `confirm-remove-all-snapshots`
* `action-aborted-snapshots-changed`
* `snapshot-removed`
* `snapshot-removed-all`
* `snapshot-restore-failed`
* `snapshot-restored`
* `command-description-snapshot-list`
* `command-description-snapshot-create`
* `command-description-snapshot-remove`
* `command-description-snapshot-restore`

### Changed messages

* Slightly changed the default messages of `type-new-name`, `name-set`, and `name-invalid`. These messages, as well as `name-has-not-changed`, can now access the new name via the argument `{name}`.

## v2.13.2

### New messages

* `cannot-trade-no-offers`
* `no-offers-open-editor-description`

## v2.13.0

The default english language file is now called `en-default`.

### New messages

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

### Changed messages

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

### Removed messages

* `no-admin-shop-type-selected`
* `no-player-shop-type-selected`

## v2.11.0

### New messages

* msg-currency-items-given
* msg-high-currency-items-given
* msg-high-currency-disabled
* msg-shop-creation-items-received
* msg-currency-items-received
* msg-high-currency-items-received
* msg-command-description-give-currency
* msg-command-description-convert-items
* msg-items-converted
* msg-button-slime-size
* msg-button-slime-size-lore
* msg-button-magma-cube-size
* msg-button-magma-cube-size-lore
* msg-unsupported-container
* msg-missing-edit-villagers-perm
* msg-missing-edit-wandering-traders-perm
* msg-must-target-entity
* msg-must-target-villager
* msg-target-entity-is-no-villager
* msg-villager-editor-title
* msg-villager-editor-description-header
* msg-villager-editor-description
* msg-button-delete-villager
* msg-button-delete-villager-lore
* msg-button-villager-inventory
* msg-button-villager-inventory-lore
* msg-button-mob-ai
* msg-button-mob-ai-lore
* msg-villager-inventory-title
* msg-set-villager-xp
* msg-no-villager-trades-changed
* msg-villager-trades-changed
* msg-command-description-edit-villager

### Changed messages

* Some message settings were renamed, but also had changes to their default contents:
  * msg-button-chest (now msg-button-container)
  * msg-button-chest-lore (now msg-button-container-lore)
  * msg-selected-chest (now msg-container-selected)
  * msg-must-select-chest (now msg-must-select-container)
  * msg-no-chest-selected (now msg-invalid-container)
  * msg-chest-too-far (now msg-container-too-far-away)
  * msg-chest-not-placed (now msg-container-not-placed)
  * msg-chest-already-in-use (now msg-container-already-in-use)
  * msg-no-chest-access (now msg-no-container-access)
  * msg-unused-chest (now msg-unused-container)
  * msg-cant-trade-with-shop-missing-chest (now msg-cant-trade-with-shop-missing-container)
* msg-creation-item-selected
* msg-shop-setup-desc-selling
* msg-shop-setup-desc-buying
* msg-shop-setup-desc-trading
* msg-shop-setup-desc-book
* msg-trade-setup-desc-selling
* msg-trade-setup-desc-buying
* msg-trade-setup-desc-book

### Removed messages

* Some messages were renamed. See above.


## v2.10.0

### New messages

* msg-button-rabbit-variant
* msg-button-rabbit-variant-lore
* msg-cant-trade-with-own-shop
* msg-cant-trade-with-shop-missing-chest

### Changed messages

* Renamed 'msg-removed-player-shops' to 'msg-removed-shops-of-player'.
* Renamed 'msg-removed-all-player-shops' to 'msg-removed-player-shops'.
* Renamed 'msg-confirm-remove-admin-shops' to 'msg-confirm-remove-all-admin-shops'.
* Renamed 'msg-confirm-remove-own-shops' to 'msg-confirm-remove-all-own-shops'.
* Renamed 'msg-confirm-remove-player-shops' to 'msg-confirm-remove-all-shops-of-player'.
* The 'msg-removed-player-shops' message (previously 'msg-removed-all-player-shops') no longer mentions that 'all' shops got deleted (since this is not necessarily true).
* Changed the 'msg-button-villager-level' and 'msg-button-villager-level-lore' messages to clarify that this option only changes the visual appearance of the villager's badge color. The included german translation has been updated accordingly as well.
* Slightly changed the german translation of the 'msg-cant-trade-while-owner-online' message.
* Removed the note about left and right clicking items to adjust amounts from the 'msg-trade-setup-desc-admin-regular' message, since this doesn't actually apply to admin shops.

## v2.9.0

### New messages

* msg-command-argument-requires-player
* msg-ambiguous-player-name
* msg-ambiguous-player-name-entry
* msg-ambiguous-player-name-more

### Changed messages

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

### Removed messages

* The default german translation contained a few no longer used messages: msg-button-type and msg-button-type-lore

## v2.8.0

No changes due to initial commit.
