from pathlib import Path

root_dir = Path(__file__).parent / "../.."
root_dir = root_dir.resolve()

target = Path(__file__).parent / "highlights.scm"

lilypond_queries = root_dir / "repos/lilypond/queries"
lilypond_scheme_queries = (
    root_dir / "repos/lilypond/tree-sitter-lilypond-scheme/queries"
)


def read_file(f: Path):
    print(f.resolve())
    return f.read_text()


def run():
    # TODO: othere stuff here crashes, find why
    lily_builtins_ = (lilypond_queries / "highlights-builtins.scm").read_text()
    lily_builtins = list(lily_builtins_.split("\n\n"))

    assert len(lily_builtins) == 18

    parts = (
        [
            read_file(lilypond_queries / "injections.scm"),
            read_file(lilypond_queries / "highlights.scm"),
        ]
        + lily_builtins[:1]
        + [
            read_file(lilypond_scheme_queries / "highlights.scm"),
            read_file(lilypond_scheme_queries / "highlights-builtins.scm"),
            read_file(lilypond_scheme_queries / "highlights-lilypond-builtins.scm"),
        ]
    )
    contents = "\n".join(parts)
    target.write_text(contents)


if __name__ == "__main__":
    run()
