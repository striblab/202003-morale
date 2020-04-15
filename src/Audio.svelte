<script>

export let booster;

</script>

{#if booster.from_strib === "TRUE"}

<div class="card strib {booster.type}">
	<h5 class="stamp">{booster.timestamp} • Star Tribune</h5>
	<audio controls>
		<source src="{booster.asset}"/>
	</audio>
	<div class="text">
		<p>{booster.story}</p>
		<a href="{booster.url}" target="_blank"><h4 class="author">Read more</h4></a>
	</div>

</div>

{:else}

<div class="card {booster.type}">
	<audio>
		<source src="{booster.asset}" controls/>
	</audio>
	<div class="text">
		<h5 class="stamp">{booster.timestamp}</h5>
		<p>{booster.story}</p>
		<h4 class="author">— {booster.name}</h4>
	</div>
</div>

{/if}
