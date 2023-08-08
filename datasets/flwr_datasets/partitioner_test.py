import unittest

from partitioner import IidPartitioner

from datasets import Dataset


class TestIidPartitioner(unittest.TestCase):
    """Test IidPartitioner."""

    def setUp(self):
        """Create a dummy dataset with 100 rows, numerical features, and labels."""
        data = {
            "features": [i for i in range(100)],
            "labels": [i % 2 for i in range(100)],
        }
        self.dataset = Dataset.from_dict(data)
        self.num_partitions = 10
        self.partition_size = self.dataset.num_rows // self.num_partitions
        self.sampler = IidPartitioner(num_partitions=self.num_partitions)

    def test_load_partition_size(self):
        partition_index = 2
        partition = self.sampler.load_partition(self.dataset, partition_index)
        self.assertEqual(partition.num_rows, self.partition_size)

    def test_load_partition_correct_data(self):
        partition_index = 2
        partition = self.sampler.load_partition(self.dataset, partition_index)
        self.assertEqual(
            partition["features"][0], partition_index * self.partition_size
        )


if __name__ == "__main__":
    unittest.main()