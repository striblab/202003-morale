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

	// local vars
	let length;
	let arr_slice_len;
	let show_more = 'Show more';
	arr_slice_len = 13;
	let booster_length;

	function handleButtonClick() {
		arr_slice_len += 6;
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

	{#if arr_slice_len < booster_length}
		<div class="showMore" on:click={handleButtonClick}>
			<p>{show_more}</p>
		</div>
	{/if}
</div>
