from pathlib import Path
from typing import Optional

import typer

app = typer.Typer(help="Trigger info access at ATLAS.")
dataset_app = typer.Typer(help="Dataset-related trigger queries.")


@dataset_app.command("list")
def list_dataset(
    data_set_name: str = typer.Argument(..., help="Dataset name to query."),
    trigger_search_times: Optional[int] = typer.Argument(
        None, help="Optional number of trigger search times."
    ),
) -> None:
    """List triggers for a dataset."""
    typer.echo("hello from atlas-trigger dataset list")


@dataset_app.command("jetpt")
def jetpt_dataset(
    dataset_did: str = typer.Argument(..., help="Rucio dataset DID to query."),
) -> None:
    """Fetch jet pT values for a dataset and write them to parquet."""
    output_path = Path.cwd() / f"{dataset_did}_jetpt.parquet"

    from func_adl_servicex_xaodr25 import FuncADLQueryPHYSLITE
    from servicex import Sample, ServiceXSpec, dataset, deliver
    from servicex_analysis_utils import to_awk
    import awkward as ak

    query = (
        FuncADLQueryPHYSLITE()
        .Select(lambda evt: {"jets": evt.Jets()})
        .Select(
            lambda collections: {
                "jet_pt": collections.jets.Select(lambda jet: jet.pt() / 1000.0),
            }
        )
    )

    delivered = deliver(
        ServiceXSpec(
            Sample=[
                Sample(
                    Name="jet_pt_fetch",
                    Dataset=dataset.Rucio(dataset_did),
                    NFiles=1,
                    Query=query,
                )
            ]
        )
    )

    arrays = to_awk(delivered)
    ak.to_parquet(arrays["jet_pt_fetch"], output_path)
    typer.echo(f"Wrote {output_path}")


app.add_typer(dataset_app, name="dataset")


def main() -> int:
    app()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
