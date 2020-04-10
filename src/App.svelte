<script>

	import { onMount } from 'svelte';
	import { intcomma } from 'journalize';
  import Photo from './Photo.svelte';
	import Text from './Text.svelte';
	import Video from './Video.svelte';
	import Audio from './Audio.svelte';
  import json from './data/data.json';

	// props
	export let boosters;
	export let featured;
	export let nonfeatured;

	$: {
		boosters = json.filter(function(d) {
      return d.publish === 'TRUE';
    })

		featured = boosters.filter(function(d) {
			return d.featured === 'TRUE';
		})

		featured = featured.reverse();

		nonfeatured = boosters.filter(function(d) {
			return d.featured !== 'TRUE';
		})

		nonfeatured = nonfeatured.reverse();

		boosters = boosters.reverse();

	}


</script>

<div class="proj-container">

		{#each boosters as booster}
			{#if booster.type === 'text'}
				<Text {booster} />
			{:else if booster.type === 'photo'}
				<Photo {booster} />
			{:else if booster.type === 'video'}
				<Video {booster} />
			{:else if booster.type === 'audio'}
				<Audio {booster} />
			{/if}
		{/each}

</div>
