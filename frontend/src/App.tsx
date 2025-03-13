import React, { useState } from "react";
import { Button, Modal, Select, Input, Spin, message } from "antd";
import axios from "axios";

const sampleSentences = [
  "বিকাশ দিয়ে বিদ্যুৎ বিল পরিশোধ করা যাবে কি?",
  "নগদ এর মাধ্যমে বিদ্যুৎ বিল দিতে চাই ।",
  "বিপিডিবি বিল জমা দিয়েছি, কিন্তু সংযোগ চালু হয়নি ।",
];

const ParaphraseApp: React.FC = () => {
  const [inputSentence, setInputSentence] = useState("");
  const [paraphrases, setParaphrases] = useState<string[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!inputSentence.trim()) {
      message.warning("Please enter or select a sentence!");
      return;
    }

    setLoading(true);
    try {
      const response = await axios.post("http://127.0.0.1:8000/paraphrase/", {
        sentence: inputSentence,
      });

      setParaphrases(response.data.paraphrases);
      setIsModalOpen(true);
    } catch (error) {
      console.error("Error fetching paraphrases:", error);
      message.error("Failed to fetch paraphrases. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center">
      <div className="bg-gradient-to-r from-blue-500 to-white p-8 rounded-2xl shadow-xl w-96 text-center">
        {/* Heading */}
        <h1 className="text-2xl font-bold text-gray-800 mb-6">Sentence Paraphraser</h1>

        {/* Input and select container */}
        <div className="mb-6 space-y-4">
          <Select
            className="w-full"
            placeholder="Select a sentence"
            onChange={setInputSentence}
            value={inputSentence || undefined}
          >
            {sampleSentences.map((sentence, index) => (
              <Select.Option key={index} value={sentence}>
                {sentence}
              </Select.Option>
            ))}
          </Select>

          <Input.TextArea
            className="w-full"
            placeholder="Or enter your own sentence"
            value={inputSentence}
            onChange={(e) => setInputSentence(e.target.value)}
            rows={4}
          />
        </div>

        {/* Submit Button */}
        <Button
          type="primary"
          onClick={handleSubmit}
          className="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition duration-300 w-full"
          disabled={loading}
        >
          {loading ? <Spin /> : "Paraphrase"}
        </Button>

        {/* Modal */}
        <Modal
          title="Paraphrased Sentences"
          open={isModalOpen}
          onCancel={() => setIsModalOpen(false)}
          footer={null}
        >
          <ul className="list-disc pl-5 text-gray-800">
            {paraphrases.map((paraphrase, index) => (
              <li key={index} className="mb-2">{paraphrase}</li>
            ))}
          </ul>
        </Modal>
      </div>
    </div>
  );
};

export default ParaphraseApp;
