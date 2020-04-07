<script>
  export let booster;

  let width = 300;
  let height = 200;

  let url = booster.asset + '?w=' + width + '&h=' + height + '&fit=crop&crop=faces';
  // let url = booster.asset + '?ar=6:4&fit=crop&crop=faces';
</script>

{#if booster.featured === "TRUE"}

<div class="card featured {booster.type}">
	<img src="{url}" alt="Smile Minnesota photo"/>
	<div class="text">
		<h5 class="stamp">{booster.timestamp}</h5>
		<p>{booster.story}</p>
		<h4 class="author">— {booster.name}</h4>
	</div>
</div>

{:else}

<div class="card {booster.type}">
	<img src="{url}" alt="Smile Minnesota photo"/>
	<div class="text">
		<h5 class="stamp">{booster.timestamp}</h5>
		<p>{booster.story}</p>
		<h4 class="author">— {booster.name}</h4>
	</div>
</div>

{/if}
