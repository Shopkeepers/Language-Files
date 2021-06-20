# Changelog v2.13.0

The default english language file is now called `en-default`.

### New messages:
* Various messages were moved from settings in the config into the language file:
  * 'editor-title'
  * 'for-hire-title'
  * 'nameplate-prefix'. Also changed the color to a dark green.
  * 'sign-shop-first-line'. This has been replaced with 8 new messages for the sign lines of different types of shops:
    * 'admin-sign-shop-line1/2/3/4'
    * 'player-sign-shop-line1/2/3/4'
    * The appearance of sign shops has changed. They are slightly more colorful now.
* Added 'must-target-container'.
* Added 'no-player-shops-via-command'.
* Added 'button-name-villager'.
* Added 'button-name-villager-lore'.
* Added 'type-new-villager-name'.
* Added 'villager-name-set'.
* Added 'villager-name-invalid'.
* Added 'button-snowman-pumpkin-head'.
* Added 'button-snowman-pumpkin-head-lore'.
* Added 'button-shulker-color'.
* Added 'button-shulker-color-lore'.
* Added 'button-invulnerability'.
* Added 'button-invulnerability-lore'.
* Added 'shops-already-removed'.
* Added 'shop-removals-cancelled'.
* Added 'shop-removed'.
* Added 'shop-already-removed'.
* Added 'shop-removal-cancelled'.
* Added 'confirm-remove-shop'.
* Added 'command-description-remove'.
* Added 'cannot-trade-unexpected-trade'.
* Added 'cannot-trade-items-not-strictly-matching'.
* Added 'cannot-trade-insufficient-storage-space'.
* Added 'cannot-trade-insufficient-currency'.
* Added 'cannot-trade-insufficient-stock'.
* Added 'cannot-trade-insufficient-writable-books'.
* Added 'trade-notification-one-item'.
* Added 'trade-notification-two-items'.
* Added 'buy-notification-one-item'.
* Added 'buy-notification-two-items'.
* Added 'trade-notification-player-shop'.
* Added 'trade-notification-named-player-shop'.
* Added 'trade-notification-admin-shop'.
* Added 'trade-notification-named-admin-shop'.
* Added 'trade-notification-trade-count'.
* Added 'owner-trade-notification-one-item'.
* Added 'owner-trade-notification-two-items'.
* Added 'owner-buy-notification-one-item'.
* Added 'owner-buy-notification-two-items'.
* Added 'owner-trade-notification-shop'.
* Added 'owner-trade-notification-named-shop'.
* Added 'owner-buy-notification-shop'.
* Added 'owner-buy-notification-named-shop'.
* Added 'owner-trade-notification-trade-count'.
* Added 'state-enabled'.
* Added 'state-disabled'.
* Added 'button-trade-notifications'.
* Added 'button-trade-notifications-lore'.
* Added 'confirmation-ui-delete-shop-title'.
* Added 'confirmation-ui-delete-shop-confirm-lore'
* Added 'confirmation-ui-confirm'.
* Added 'confirmation-ui-cancel'.
* Added 'confirmation-ui-cancel-lore'.
* Added 'confirmation-ui-aborted'.
* Added 'villager-no-longer-exists'.
* Added 'confirmation-ui-delete-villager-title'.
* Added 'confirmation-ui-delete-villager-confirm-lore'.
* Added 'villager-removed'.
* Added 'button-sign-glowing-text'.
* Added 'button-sign-glowing-text-lore'.
* Added 'button-axolotl-variant'.
* Added 'button-axolotl-variant-lore'.
* Added 'button-glow-squid-dark'.
* Added 'button-glow-squid-dark-lore'.
* Added 'button-goat-screaming'.
* Added 'button-goat-screaming-lore'.

### Changed messages:
* All message keys were changed to no longer start with the 'msg' prefix.
* Renamed 'cant-hire' -> 'cannot-hire'.
* Renamed 'cant-hire-shop-type' -> 'cannot-hire-shop-type'.
* Renamed 'cant-trade-with-own-shop' -> 'cannot-trade-with-own-shop'.
* Renamed 'cant-trade-while-owner-online' -> 'cannot-trade-while-owner-online'.
* Renamed 'cant-trade-with-shop-missing-container' -> 'cannot-trade-with-shop-missing-container'.
* Changed the default color of 'villager-editor-title' to be less bright.
* Changed the 'too-many-shops' message to be more general.
* Changed 'creation-item-selected' to clarify that one has to not aim at any block in order to select the shop or object type.
* Renamed and slightly changed 'command-description-remove' -> 'command-description-remove-all'.
* Slightly changed the default 'command-description-list' message.
* Renamed and slightly changed 'removed-admin-shops' -> 'admin-shops-removed'.
* Renamed and slightly changed 'removed-shops-of-player' -> 'shops-of-player-removed'.
* Renamed and slightly changed 'removed-player-shops' -> 'shops-of-player-removed'.
* Changed 'owner-set'.
* Changed 'set-for-hire'.
* Small fix in 'confirm-remove-all-admin-shops'.
* Small fix in 'confirm-remove-all-own-shops'.
* Small fix in 'confirm-remove-all-shops-of-player'.
* Small fix in 'confirm-remove-all-player-shops'.

### Removed messages:
* Removed 'no-admin-shop-type-selected'.
* Removed 'no-player-shop-type-selected'.
