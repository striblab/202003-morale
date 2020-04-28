<script>

  export let booster;

  let w = 300;
  let h = 400;

</script>

  {#if booster.from_strib === "TRUE"}

    {#if booster.shape === "Portrait"}

      {#if booster.long === "TRUE"}

        <div class="card strib {booster.type} portrait long">
          <h5 class="stamp">{booster.timestamp}</h5>
          <video height="400" src="{booster.asset}" controls>
            <source src="{booster.asset}" type="video/mp4">
            <source src="{booster.asset}" type="video/quicktime">
          </video>
          <div class="text">
            <p>{@html booster.story} <a href="{booster.url}" target="_blank">Read more</a></p>
          <h4 class="author">{booster.name}, Star Tribune</h4>
          </div>
        </div>

      {:else}

        <div class="card strib {booster.type} portrait">
          <h5 class="stamp">{booster.timestamp}</h5>
          <video height="400" src="{booster.asset}" controls>
            <source src="{booster.asset}" type="video/mp4">
            <source src="{booster.asset}" type="video/quicktime">
          </video>
          <div class="text">
            <p>{@html booster.story} <a href="{booster.url}" target="_blank">Read more</a></p>
          <h4 class="author">{booster.name}, Star Tribune</h4>
          </div>
        </div>

      {/if}

    {:else}

      {#if booster.long === "TRUE"}
        <div class="card strib {booster.type} landscape long">
          <h5 class="stamp">{booster.timestamp}</h5>

          <video height="300" src="{booster.asset}" controls>
            <source src="{booster.asset}" type="video/mp4">
          </video>
          <div class="text">
             <p>{@html booster.story} <a href="{booster.url}" target="_blank">Read more</a></p>
          <h4 class="author">{booster.name}, Star Tribune</h4>
          </div>

        </div>
      {:else}
      <div class="card strib {booster.type} landscape">
          <h5 class="stamp">{booster.timestamp}</h5>

          <video height="300" src="{booster.asset}" controls>
            <source src="{booster.asset}" type="video/mp4">
          </video>
          <div class="text">
             <p>{@html booster.story} <a href="{booster.url}" target="_blank">Read more</a></p>
          <h4 class="author">{booster.name}, Star Tribune</h4>
          </div>

        </div>
      {/if}

    {/if}

  {:else}

    {#if booster.shape === "Portrait"}

      {#if booster.long === "TRUE"}

        <div class="card strib {booster.type} portrait long">
          <h5 class="stamp">{booster.timestamp}</h5>
          <video height="400" src="{booster.asset}" controls>
            <source src="{booster.asset}" type="video/mp4">
            <source src="{booster.asset}" type="video/quicktime">
          </video>
          <div class="text">
            <p>{@html booster.story} <a href="{booster.url}" target="_blank">Read more</a></p>
          <h4 class="author">{booster.name}, {booster.city}</h4>
          </div>
        </div>

      {:else}

        <div class="card strib {booster.type} portrait">
          <h5 class="stamp">{booster.timestamp}</h5>
          <video height="400" src="{booster.asset}" controls>
            <source src="{booster.asset}" type="video/mp4">
            <source src="{booster.asset}" type="video/quicktime">
          </video>
          <div class="text">
            <p>{@html booster.story} <a href="{booster.url}" target="_blank">Read more</a></p>
          <h4 class="author">{booster.name}, {booster.city}</h4>
          </div>
        </div>

      {/if}

    {:else}

      {#if booster.long === "TRUE"}
        <div class="card strib {booster.type} landscape long">
          <h5 class="stamp">{booster.timestamp}</h5>

          <video height="300" src="{booster.asset}" controls>
            <source src="{booster.asset}" type="video/mp4">
          </video>
          <div class="text">
             <p>{@html booster.story} <a href="{booster.url}" target="_blank">Read more</a></p>
          <h4 class="author">{booster.name}, {booster.city}</h4>
          </div>

        </div>
      {:else}
      <div class="card strib {booster.type} landscape">
          <h5 class="stamp">{booster.timestamp}</h5>

          <video height="300" src="{booster.asset}" controls>
            <source src="{booster.asset}" type="video/mp4">
          </video>
          <div class="text">
             <p>{@html booster.story} <a href="{booster.url}" target="_blank">Read more</a></p>
          <h4 class="author">{booster.name}, {booster.city}</h4>
          </div>

        </div>
      {/if}

    {/if}

  {/if}
