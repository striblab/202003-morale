import App from './App.svelte';
import './scss/style.scss';


const app = new App({
	target: document.querySelector('#project-container'),
	props: {
		'title': 'Morale Boosters'
	}
});

window.app = app;

export default app;
