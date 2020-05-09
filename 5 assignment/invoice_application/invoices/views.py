from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import (ListView, DetailView, CreateView, View, UpdateView)
from invoices.models import Invoice, Form
from io import BytesIO

class InvoiceCreateView(CreateView):
	model = Invoice
	template_name = "create_invoice.html"
	fields = ['id', 'name', 'measurement', 'amount', 'sum', 'location']

	def form_valid(self, form):
		form.instance.form = Form.objects.get(pk=self.kwargs['pk'])
		form.instance.cost = form.instance.sum / form.instance.amount
		return super().form_valid(form)

class InvoiceUpdateView(UpdateView):
	model = Invoice
	template_name = "update_invoice.html"
	fields = ['id', 'name', 'measurement', 'amount', 'sum', 'location']

	def form_valid(self, form):
		form.instance.invoice = Invoice.objects.get(pk=self.kwargs['pk'])
		return super().form_valid(form)

class FormCreateView(CreateView):
	model = Form
	template_name = "create_form.html"
	fields = ['company', 'order_approval_number', 'established_at', 'approved_at', 'commisioner_1', 'commisioner_2',
			  'commisioner_3', 'commisioner_4', 'purchase_doc_seller', 'purchase_doc_number',
			  'purchase_doc_serial', 'purchase_doc_at']

	def form_valid(self, form):
		form.instance.responsible_user = self.request.user
		return super().form_valid(form)

class FormUpdateView(UpdateView):
	model = Form
	template_name = "update_form.html"
	fields = ['company', 'order_approval_number', 'established_at', 'approved_at', 'commisioner_1', 'commisioner_2',
			  'commisioner_3', 'commisioner_4', 'purchase_doc_seller', 'purchase_doc_number',
			  'purchase_doc_serial', 'purchase_doc_at']

class FormListView(ListView):
	model = Form
	template_name = 'list_form.html'

	def get_context_data(self, *args, **kwargs):
		context = super(FormListView, self).get_context_data(*args, **kwargs)
		context['forms'] = Form.objects.all()
		return context


class FormDetailsView(DetailView):
	model = Form
	template_name = 'details_form.html'

	def get(self, request, *args, **kwargs):
		f = Form.objects.get(pk=self.kwargs['pk'])
		self.object = self.get_object()
		context = self.get_context_data(object=self.object)
		return self.render_to_response(context)

	def get_context_data(self, **kwargs):
		context = super(FormDetailsView, self).get_context_data(**kwargs)
		f = Form.objects.get(pk=self.kwargs['pk'])
		context['invoices'] = f.invoice_set.all()
		return context

class GeneratePDF(View):
	def get(self, request, *args, **kwargs):
		form = Form.objects.get(pk=kwargs['pk'])
		data = vars(form)
		data['approved_at_year'] = str(data['approved_at'].strftime('%Y'))
		data['approved_at_month'] = str(data['approved_at'].strftime('%m'))
		data['approved_at_day'] = str(data['approved_at'].strftime('%d'))
		data['approved_at'] = str(data['approved_at'].strftime('%Y-%m-%d'))
		data['purchase_doc_at'] = str(data['purchase_doc_at'].strftime('%Y %m %d'))
		if form.commisioner_1 != None:
			data['commisioner1_name'] = form.commisioner_1.name + " " + form.commisioner_1.surname
			data['commisioner1_obligation'] = form.commisioner_1.obligation
		else:
			data['commisioner1_name'] = ""
			data['commisioner1_obligation'] = ""

		if form.commisioner_2 != None:
			data['commisioner2_name'] = form.commisioner_2.name + " " + form.commisioner_2.surname
			data['commisioner2_obligation'] = form.commisioner_2.obligation
		else:
			data['commisioner2_name'] = ""
			data['commisioner2_obligation'] = ""

		if form.commisioner_3 != None:
			data['commisioner3_name'] = form.commisioner_3.name + " " + form.commisioner_3.surname
			data['commisioner3_obligation'] = form.commisioner_3.obligation
		else:
			data['commisioner3_name'] = ""
			data['commisioner3_obligation'] = ""

		if form.commisioner_4 != None:
			data['commisioner4_name'] = form.commisioner_4.name + " " + form.commisioner_4.surname
			data['commisioner4_obligation'] = form.commisioner_4.obligation
		else:
			data['commisioner4_name'] = ""
			data['commisioner4_obligation'] = ""
		data['user_name'] = form.responsible_user.name + " " + form.responsible_user.surname
		data['user_location'] = form.responsible_user.location
		total_sum = 0
		for a in form.invoice_set.all():
			total_sum = total_sum + a.sum
		data['total_sum'] = total_sum
		data['invoices'] = form.invoice_set.all()
		pdf = render_to_pdf('Aktas.html', data)

		return HttpResponse(pdf, content_type='application/pdf')

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("windows-1257")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None
