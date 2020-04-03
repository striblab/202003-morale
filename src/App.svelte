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

		console.log(boosters)
	}


</script>

<div class="proj-container">


</div>
