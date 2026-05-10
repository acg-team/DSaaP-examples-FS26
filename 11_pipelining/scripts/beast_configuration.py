import os
import xml.etree.ElementTree as ET
import re
import argparse
from dark.fasta import FastaReads


def sanitize_id(name):
    # Replace non-alphanumeric characters with underscore
    return re.sub(r"[^a-zA-Z0-9_]", "_", name)


def generate_beast_config(alignment_path, template_path, output_path):
    print(f"Processing {alignment_path}...")

    # Determine character set
    char_count = 4 if "DNA" in alignment_path else 20

    # Parse alignment
    if isinstance(alignment_path, str):
        if not os.path.isfile(alignment_path):
            raise ValueError(
                f"{alignment_path} must be a path to a fasta file or a dark.Reads object."
            )
        sequences = FastaReads(alignment_path)
    else:
        sequences = alignment_path

    # Parse template
    try:
        tree = ET.parse(template_path)
        root = tree.getroot()
    except Exception as e:
        print(f"Error parsing template {template_path}: {e}")
        return

    data_element = root.find("data")

    if data_element is None:
        print(f"Could not find data element in {template_path}")
        return

    # Update ID based on alignment filename
    old_id = data_element.get("id")
    if old_id:
        if isinstance(alignment_path, str):
            new_id = os.path.splitext(os.path.basename(alignment_path))[0]
        else:
            new_id = "alignment"

        # Update the data element ID
        data_element.set("id", new_id)

        # Update references in all other elements
        for elem in root.iter():
            for attr, value in elem.attrib.items():
                if value and old_id in value:
                    elem.set(attr, value.replace(old_id, new_id))

    for read in sequences:
        name = read.id
        seq = read.sequence
        # Create sequence element
        # <sequence id="seq_{name}" spec="Sequence" taxon="{name}" totalcount="{count}" value="{seq}"/>
        seq_elem = ET.Element("sequence")
        safe_name = sanitize_id(name)
        seq_elem.set("id", f"seq_{safe_name}")
        seq_elem.set("spec", "Sequence")
        seq_elem.set("taxon", name)
        seq_elem.set("totalcount", f"{char_count}")
        seq_elem.set("value", seq)

        # Determine indentation - try to match template style if possible,
        # but ElementTree formatting isn't great.
        # We can just append.
        data_element.append(seq_elem)

    try:
        # Format XML
        if hasattr(ET, "indent"):
            ET.indent(tree, space="    ", level=0)

        # Check if output directory exists
        if os.path.dirname(output_path):
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

        tree.write(output_path, encoding="UTF-8", xml_declaration=True)
        print(f"Generated {output_path}")
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate BEAST2 configuration files from alignments."
    )
    parser.add_argument(
        "--alignment", "-a", help="Path to the alignment file (e.g., .fasta, .aln)."
    )
    parser.add_argument(
        "--template",
        "-t",
        help="Path to the BEAST2 template XML file. If not provided, a default template will be used based on the alignment type.",
    )
    parser.add_argument("--output", "-o", help="Path to the output XML file.")

    args = parser.parse_args()

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if args.alignment is None:
        print("No alignment file provided. Exiting.")
        return

    default_template_path = (
        os.path.join(repo_root, "beast_template", "dna_template.xml")
        if "DNA" in args.alignment
        else os.path.join(repo_root, "beast_template", "protein_template.xml")
    )

    alignment_path = args.alignment
    template_path = args.template if args.template else default_template_path

    if args.output:
        output_path = args.output
    else:
        # Default output path if not specified: append .xml to alignment filename
        output_path = alignment_path + ".xml"

    generate_beast_config(alignment_path, template_path, output_path)


if __name__ == "__main__":
    main()
