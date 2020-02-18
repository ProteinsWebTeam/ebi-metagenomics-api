import os
import unittest

from emgapianns.management.lib.downloadable_files import ChunkedDownloadFiles, UnchunkedDownloadFile
from emgapianns.management.webuploader_configs import get_downloadset_config


class ChunkedDownloadFilesTest(unittest.TestCase):

    def test_download_files(self):
        input_file_name = "ERR3477396_MERGED_FASTQ"
        root_dir = os.path.dirname(__file__)
        result_dir = os.path.join(root_dir, "test-inputs", input_file_name)

        config = get_downloadset_config("4.1", "WGS")
        for file_config in config:
            if file_config['downloadable']:
                if file_config['_chunked']:
                    f = ChunkedDownloadFiles(file_config, result_dir, input_file_name)
                    if file_config['description_label'] == "Reads encoding SSU rRNA":
                        assert f.parent_file is None
                        assert 1 == len(f.chunked_files)
                        assert "ERR3477396_MERGED_FASTQ_SSU.fasta.gz" == f.chunked_files[0].alias
                        assert "SSU.fasta.gz" == f.chunked_files[0].realname
                        assert "sequence-categorisation" == f.chunked_files[0].sub_dir
                    elif file_config['description_label'] == "Processed nucleotide reads":
                        assert f.parent_file is not None
                        assert 4 == len(f.chunked_files)
                        assert "ERR3477396_MERGED_FASTQ_3.fasta.gz" == f.chunked_files[1].alias
                        assert "ERR3477396_MERGED_FASTQ_3.fasta.gz" == f.chunked_files[1].realname
                        assert "" == f.chunked_files[1].sub_dir
                else:
                    f = UnchunkedDownloadFile(file_config, result_dir, input_file_name)
                    if file_config['description_label'] == "GO slim annotation":
                        assert "ERR3477396_MERGED_FASTQ_summary.go_slim" == f.realname
                        assert "ERR3477396_MERGED_FASTQ_GO_slim.csv" == f.alias
                        assert "" == f.sub_dir
