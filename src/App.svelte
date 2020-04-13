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

	<div class="intro-text">
		<p>Do you have something good to share? <a href="https://www.startribune.com/x/569251431">Send us your morale booster here</a> for a chance to be published below.</p>
	</div>

	<div class="cards-grid">
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
</div>
