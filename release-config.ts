export default {
    changeTypes: [
        {
            title: '💥 Breaking changes',
            labels: ['Docs:Breaking-Change'],
            bump: 'major',
            weight: 4,
        },
        {
            title: ':octocat: Developer Documentation',
            labels: ['Docs:Developer'],
            bump: 'minor',
            weight: 3,
        },
        {
            title: '🐾 Guides',
            labels: ['Docs:Guides'],
            bump: 'minor',
            weight: 2,
        },
        {
            title: '👷 Admin Documentation',
            labels: ['Docs:Admin'],
            bump: 'minor',
            weight: 1,
        },
        {
            title: '👤 User Documentation',
            labels: ['Docs:User'],
            bump: 'minor',
        },
        {
            title: '🐛 Bug Fixes',
            labels: ['Type:Bug'],
            bump: 'patch',
        },
        {
            title: '📦️ Build&Tools',
            labels: ['dependency', 'dependencies', 'Docs:Build&Tools'],
            bump: 'patch',
            weight: -1,
        },
    ],
};
