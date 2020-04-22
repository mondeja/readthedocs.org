from django.test import TestCase, override_settings

from readthedocs.rtd_tests.tests.test_resolver import ResolverBase
from readthedocs.core.unresolver import unresolve


@override_settings(
    PRODUCTION_DOMAIN='readthedocs.org',
    PUBLIC_DOMAIN='readthedocs.io',
    RTD_EXTERNAL_VERSION_DOMAIN='dev.readthedocs.build',
    PUBLIC_DOMAIN_USES_HTTPS=True,
    USE_SUBDOMAIN=True,
)
class UnResolverTests(ResolverBase):

    def test_unresolver(self):
        parts = unresolve('http://pip.readthedocs.io/en/latest/foo.html')
        self.assertEqual(parts[0].slug, 'pip')
        self.assertEqual(parts[1], 'en')
        self.assertEqual(parts[2], 'latest')
        self.assertEqual(parts[3], 'foo.html')

    def test_unresolver_subproject(self):
        parts = unresolve('http://pip.readthedocs.io/projects/sub/ja/latest/foo.html')
        self.assertEqual(parts[0].slug, 'sub')
        self.assertEqual(parts[1], 'ja')
        self.assertEqual(parts[2], 'latest')
        self.assertEqual(parts[3], 'foo.html')

    def test_unresolver_translation(self):
        parts = unresolve('http://pip.readthedocs.io/ja/latest/foo.html')
        self.assertEqual(parts[0].slug, 'trans')
        self.assertEqual(parts[1], 'ja')
        self.assertEqual(parts[2], 'latest')
        self.assertEqual(parts[3], 'foo.html')
