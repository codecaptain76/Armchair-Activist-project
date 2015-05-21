<form method="post" action="https://api.ammado.com/v1/donate" accept-charset="utf-8">
	<div>
		<label for="donorEmail">Email:</label>
		<input type="email" name="donorEmail" id="donorEmail" value="" />
	</div>

	<fieldset>
		<div>
			<input type="radio" name="donationAmount" id="amount10" value="10" />
			<label for="amount10">€10</label>
		</div>

		<div>
			<input type="radio" name="donationAmount" id="amount25" value="25" />
			<label for="amount25">€25</label>
		</div>

		<div>
			<input type="radio" name="donationAmount" id="amount50" value="50" />
			<label for="amount50">€50</label>
		</div>

		<div>
			<input type="radio" name="donationAmount" id="amountOther" value="" />
			<label for="amountOther">Other</label>
			<input type="number" min="4" max="20000"
					name="donationAmount" id="customAmount" />
		</div>
	</fieldset>
	<input type="hidden" name="currencyCode" value="EUR" />
	<input type="hidden" name="beneficiaryId" value="112794" />
	<input type="hidden" name="apiKey" value="C41E20A0-E2B4-4F16-A414-401DBAC282BD" />
	
	<button type="submit">Donate</button>
</form>
<script>
	// example of how pre-defined amounts can be handled in JS
	var handleClick = function(e)
	{
		if (!e) var e = window.event;
		var input = e.target || e.srcElement;
		if (input.name == 'donationAmount')
		{
			var custom = document.getElementById('customAmount');
			if (input.id == 'amountOther')
			{
				custom.removeAttribute('disabled');
				custom.focus();
			}
			else if (input.id != 'customAmount')
			{
				custom.setAttribute('disabled', 'disabled');
			}
		}
	}
	var inputs = document.getElementsByTagName('input');
	for (var i = inputs.length - 1; i >= 0; i--)
	{
		inputs[i].onclick=handleClick;
	}
	
	// only disable the input if Javascript is available!
	if (!document.getElementById('amountOther').checked) {
		document.getElementById('customAmount').setAttribute('disabled', 'disabled');
	}
</script>