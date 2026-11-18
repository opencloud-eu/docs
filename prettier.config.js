module.exports = {
    ...require("@opencloud-eu/prettier-config"),
    semi: true,
    overrides: [
        {
            files: ["docs/dev/web/**", "versioned_docs/*/dev/web/**"],
            options: { semi: false }
        }
    ]
};
