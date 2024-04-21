from project_composer.marker import EnabledApplicationMarker


class FobiDefinitions(EnabledApplicationMarker):
    def define(self):
        return super().define() + [
            [
                "fobi",
                {
                    "comments": "Fobi",
                    "natural_foreign": True,
                    "models": [
                        "fobi.FormElement_users",
                        "fobi.FormElement_groups",
                        "fobi.FormElement",
                        "fobi.FormHandler_users",
                        "fobi.FormHandler_groups",
                        "fobi.FormHandler",
                        # "fobi.FormWizardHandler_users",
                        # "fobi.FormWizardHandler_groups",
                        # "fobi.FormWizardHandler",
                        # "fobi.FormWizardEntry",
                        "fobi.FormEntry",
                        # "fobi.FormWizardFormEntry",
                        "fobi.FormFieldsetEntry",
                        "fobi.FormElementEntry",
                        "fobi.FormHandlerEntry",
                        # "fobi.FormWizardHandlerEntry"
                    ]
                }
            ],
            [
                "fobi.contrib.plugins.form_handlers.db_store",
                {
                    "comments": "Fobi_Contrib_Plugins_Form_Handlers_Db_Store",
                    "natural_foreign": True,
                    "models": [
                        (
                            "fobi_contrib_plugins_form_handlers_db_store."
                            "SavedFormDataEntry"
                        ),
                        # (
                        #     "fobi_contrib_plugins_form_handlers_db_store."
                        #     "SavedFormWizardDataEntry"
                        # )
                    ]
                }
            ],
        ]
