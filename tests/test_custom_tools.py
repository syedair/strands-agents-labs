"""Unit tests for custom tools defined in labs 4a and 4b."""

from unittest.mock import patch


# ── Lab 4a: word_count tool ────────────────────────────────────────────────


def word_count(text: str) -> int:
    """Inline copy of the tool logic so tests don't require a running model."""
    return len(text.split())


class TestWordCount:
    def test_simple_sentence(self):
        assert word_count("How many words are in this sentence?") == 7

    def test_single_word(self):
        assert word_count("hello") == 1

    def test_empty_string(self):
        assert word_count("") == 0

    def test_extra_whitespace(self):
        # str.split() with no args collapses any whitespace
        assert word_count("  hello   world  ") == 2

    def test_multiline_text(self):
        assert word_count("line one\nline two\nline three") == 6


# ── Lab 4b: websearch tool ─────────────────────────────────────────────────


def websearch(keywords: str, region: str = "us-en", max_results: int | None = None) -> str:
    """Inline copy of the tool logic so tests don't require network access."""
    from ddgs import DDGS
    from ddgs.exceptions import RatelimitException

    try:
        results = DDGS().text(keywords, region=region, max_results=max_results)
        return results if results else "No results found."
    except RatelimitException:
        return "RatelimitException: Please try again after a short delay."
    except Exception as e:
        return f"Exception: {e}"


class TestWebsearch:
    def test_returns_results(self):
        mock_results = [{"title": "Recipe", "body": "Chicken broccoli stir-fry"}]
        with patch("ddgs.DDGS.text", return_value=mock_results):
            result = websearch("chicken broccoli recipe")
        assert result == mock_results

    def test_no_results(self):
        with patch("ddgs.DDGS.text", return_value=None):
            result = websearch("xyznonexistent12345")
        assert result == "No results found."

    def test_rate_limit_exception(self):
        from ddgs.exceptions import RatelimitException

        with patch("ddgs.DDGS.text", side_effect=RatelimitException()):
            result = websearch("python recipes")
        assert "RatelimitException" in result

    def test_generic_exception(self):
        with patch("ddgs.DDGS.text", side_effect=RuntimeError("network error")):
            result = websearch("any query")
        assert "Exception" in result
        assert "network error" in result

    def test_region_parameter(self):
        mock_results = [{"title": "UK Recipe", "body": "Chicken dish"}]
        with patch("ddgs.DDGS.text", return_value=mock_results) as mock_search:
            websearch("chicken recipe", region="uk-en", max_results=5)
            mock_search.assert_called_once_with(
                "chicken recipe", region="uk-en", max_results=5
            )
