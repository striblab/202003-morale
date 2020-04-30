<script>
	import { watchResize } from "svelte-watch-resize";
	import { writable } from 'svelte/store';
	import { onMount, onDestroy } from 'svelte';
	import { intcomma } from 'journalize';
  import Photo from './Photo.svelte';
	import Text from './Text.svelte';
	import Video from './Video.svelte';
	import Audio from './Audio.svelte';
	import Lightbox from './Lightbox.svelte';
  import json from './data/data.json';

	const Masonry = require('masonry-layout');

	const store = writable()

	let lightbox_booster;

	$: {
		store.subscribe(value => {
			lightbox_booster = value;
		})
	}

	// props
	export let boosters;

	// local vars
	let window_width;
	let length;
	let arr_slice_len;
	let show_more = 'Show more';
	arr_slice_len = 13;
	let booster_length;

	function handleButtonClick() {
		arr_slice_len += 6;
	}

	function close() {
		var box = document.querySelector('.lightbox');
		box.style.display = 'none'

		store.set()
	}

	function resize() {
		let screen = window.innerWidth
		console.log(screen)
	}

	$: {

		booster_length = json.filter(function(d) {
      return d.publish === 'TRUE';
    }).length

		boosters = json.filter(function(d) {
      return d.publish === 'TRUE';
    })

		boosters = boosters.reverse();

		boosters = boosters.slice(0, arr_slice_len);

	}

	onMount(async () => {
		var msnry = new Masonry( '.cards-grid', {
		  columnWidth: 200,
		  itemSelector: '.card'
		});
	});



</script>

<svelte:window bind:innerWidth={window_width} />

<div class="proj-container">

	<div class="intro-text">
		<p>Do you have something good to share? <a href="https://www.startribune.com/x/569251431">Send us your morale booster here</a> for a chance to be published below.</p>
	</div>

	<div class="cards-grid">
		{#each boosters as booster}
			{#if booster.type === 'text'}
				<Text {booster} {store} {window_width}/>
			{:else if booster.type === 'photo'}
				<Photo {booster} {store} {window_width}/>
			{:else if booster.type === 'video'}
				<Video {booster} {store} {window_width}/>
			{:else if booster.type === 'audio'}
				<Audio {booster} {store}/>
			{/if}
		{/each}
	</div>

	<div class="lightbox" style="display:none;">
		<span class="close cursor" on:click={close}>&times;</span>
		{#if lightbox_booster}
		<div class="lightboxWrapper">
			<Lightbox {lightbox_booster} {store}/>
		</div>
		{/if}
	</div>

	{#if arr_slice_len < booster_length}
		<div class="showMore" on:click={handleButtonClick}>
			<p>{show_more}</p>
		</div>
	{/if}
</div>
