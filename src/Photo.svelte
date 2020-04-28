<script>
  export let booster;

  let pWidth = 600;
  let pHeight = 1000;

  let lWidth = 1000;
  let lHeight = 600;

  let pUrl = booster.asset + '?w=' + pWidth + '&h=' + pHeight + '&fit=crop&crop=faces&max-h=900';
  let lUrl = booster.asset + '?w=' + lWidth + '&h=' + lHeight + '&fit=crop&crop=faces&max-h=600';
</script>

<style>

</style>

{#if booster.from_strib === "TRUE"}

  {#if booster.shape === "Portrait"}

    <div class="card strib {booster.type} portrait">
      <h5 class="stamp">{booster.timestamp}</h5>
      <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({pUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
      <div class="text">
        <p>{@html booster.story} <a href="{booster.url}" target="_blank">Read more</a></p>
        <h4 class="author">{booster.name}, Star Tribune</h4>
      </div>
    </div>

  {:else}

    <div class="card strib {booster.type} landscape">
      <h5 class="stamp">{booster.timestamp}</h5>
       <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({lUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
      <div class="text">
        <p>{@html booster.story} <a href="{booster.url}" target="_blank">Read more</a></p>
        <h4 class="author">{booster.name}, Star Tribune</h4>
      </div>
    </div>

  {/if}



{:else}

  {#if booster.shape === "Portrait"}

    <div class="card {booster.type} portrait">
      <h5 class="stamp">{booster.timestamp}</h5>
       <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({pUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
      <div class="text">
        <p>{@html booster.story}</p>
        <h4 class="author">{booster.name}, {booster.city}</h4>
      </div>
    </div>

  {:else}

    <div class="card {booster.type} landscape">
      <h5 class="stamp">{booster.timestamp}</h5>
       <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({lUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
      <div class="text">
        <p>{@html booster.story}</p>
        <h4 class="author">{booster.name}, {booster.city}</h4>
      </div>
    </div>

  {/if}

{/if}
