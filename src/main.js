import App from './App.svelte';

const app = new App({
	target: document.querySelector('.l-article .l-article-body .l-container'),
	props: {
		'title': 'Morale Boosters'
	}
});

window.app = app;

export default app;
