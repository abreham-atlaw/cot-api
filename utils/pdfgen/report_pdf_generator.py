import typing
import uuid

from apps.core.models import Summary
from apps.core.serializers import SummarySerializer
from cot.settings import BMC_EXPORT_PATH
from .generator import PDFGenerator


class ReportPDFGenerator(PDFGenerator):

	def _generate_name(self) -> str:
		return BMC_EXPORT_PATH/f"{uuid.uuid4()}.pdf"

	def generate_bmc(self, context: typing.Dict):

		export_path = self._generate_name()

		self.generate(
			"res/pdf_templates/report.html",
			context,
			outpath=export_path
		)

		return export_path
