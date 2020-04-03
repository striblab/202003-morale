<script>

	import { onMount } from 'svelte';
	import { intcomma } from 'journalize';
  import Photo from './Photo.svelte';
	import Text from './Text.svelte';
	import Video from './Video.svelte';
	import Audio from './Audio.svelte';
  import json from './data/data.json';

	// props
	export let boosters

	$: {
		boosters = json.filter(function(d) {
      return d.publish === 'TRUE';
    })

		boosters = boosters.reverse();
	}


</script>

<div class="proj-container">

	{#each boosters as booster}
		{#if booster.type === 'text'}
			<p>text</p>
		{:else if booster.type === 'photo'}
			<Photo {booster}/>
		{:else if booster.type === 'video'}
			<Video {booster}/>
		{:else if booster.type === 'audio'}
			<p>audio</p>
		{/if}
	{/each}

</div>
