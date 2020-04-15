<script>
  export let booster;

  let pWidth = 600;
  let pHeight = 1000;

  let lWidth = 1000;
  let lHeight = 600;

  let pUrl = booster.asset + '?w=' + pWidth + '&h=' + pHeight + '&fit=crop&crop=faces&max-h=900';
  let lUrl = booster.asset + '?w=' + lWidth + '&h=' + lHeight + '&fit=crop&crop=faces&max-h=600';
</script>

{#if booster.from_strib === "TRUE"}

  {#if booster.shape === "Portrait"}

    <div class="card strib {booster.type} portrait">
      <h5 class="stamp">{booster.timestamp} • <span class="green">Star Tribune</span></h5>
      <img src="{pUrl}" alt="Smile Minnesota photo"/>
      <div class="text">
        <p>{booster.story}</p>
        <a href="{booster.url}" target="_blank"><h4 class="author">Read more</h4></a>
      </div>
    </div>

  {:else}

    <div class="card strib {booster.type} landscape">
      <h5 class="stamp">{booster.timestamp} • <span class="green">Star Tribune</span></h5>
      <img src="{lUrl}" alt="Smile Minnesota photo"/>
      <div class="text">
        <p>{booster.story}</p>
        <a href="{booster.url}" target="_blank"><h4 class="author">Read more</h4></a>
      </div>
    </div>

  {/if}



{:else}

  {#if booster.shape === "Portrait"}

    <div class="card {booster.type} portrait">
      <h5 class="stamp">{booster.timestamp}</h5>
      <img src="{pUrl}" alt="Smile Minnesota photo"/>
      <div class="text">
        <p>{booster.story}</p>
        <h4 class="author">— {booster.name}</h4>
      </div>
    </div>

  {:else}

    <div class="card {booster.type} landscape">
      <h5 class="stamp">{booster.timestamp}</h5>
      <img src="{lUrl}" alt="Smile Minnesota photo"/>
      <div class="text">
        <p>{booster.story}</p>
        <h4 class="author">— {booster.name}</h4>
      </div>
    </div>

  {/if}

{/if}
