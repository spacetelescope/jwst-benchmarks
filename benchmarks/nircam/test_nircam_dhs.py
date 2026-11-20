import os

import pytest

from jwst.stpipe import Step

# Mark all tests in this module
pytestmark = [pytest.mark.bigdata]


def test_nircam_dhs_sw_det1(_jail, resource_tracker, request):
    """Run calwebb_detector1 on NIRCam imaging long data"""
    uncal_file = os.environ["TEST_BIGDATA"] + "jwst-pipeline/dev/nircam/dhs/jw04453010001_02106_00001_nrca1_genheader_uncal.fits"

    # Run detector1 pipeline only on one of the _uncal files
    args = [
        "calwebb_detector1",
        uncal_file,
        "--steps.dq_init.save_results=True",
        "--steps.saturation.save_results=True",
        "--steps.superbias.save_results=True",
        "--steps.refpix.save_results=True",
        "--steps.linearity.save_results=True",
        "--steps.dark_current.save_results=True",
        "--steps.jump.save_results=True",
        "--steps.jump.rejection_threshold=50.0",
        f"--output_dir={os.path.abspath(os.curdir)}",
    ]
    with resource_tracker.track(log=request):
        Step.from_cmdline(args)


def test_nircam_dhs_lw_det1(_jail, resource_tracker, request):
    """Run calwebb_detector1 on NIRCam DHS long-wave data"""
    uncal_file = os.environ["TEST_BIGDATA"] + "jwst-pipeline/dev/nircam/dhs/jw04453010001_02106_00001_nrcalong_genheader_uncal.fits"

    # Run detector1 pipeline only on one of the _uncal files
    args = [
        "calwebb_detector1",
        uncal_file,
        "--steps.dq_init.save_results=True",
        "--steps.saturation.save_results=True",
        "--steps.superbias.save_results=True",
        "--steps.refpix.save_results=True",
        "--steps.linearity.save_results=True",
        "--steps.dark_current.save_results=True",
        "--steps.jump.save_results=True",
        "--steps.jump.rejection_threshold=50.0",
        f"--output_dir={os.path.abspath(os.curdir)}",
    ]
    with resource_tracker.track(log=request):
        Step.from_cmdline(args)


def test_nircam_dhs_sw_stripe1_spec2(_jail, resource_tracker, request):
    """Run calwebb_spec2 on NIRCam DHS short-wave data using a STRIPE1 subarray"""
    rateints_file = os.environ["TEST_BIGDATA"] + "jwst-pipeline/dev/nircam/dhs/jw04453029001_02102_00001-seg001_nrca2_rateints.fits"

    # Run spec2 pipeline on rateints file
    args = [
        "calwebb_spec2",
        rateints_file,
        "--steps.assign_wcs.save_results=True",
        "--steps.extract_2d.save_results=True",
        "--steps.extract_1d.save_results=True",
        f"--output_dir={os.path.abspath(os.curdir)}",
    ]
    with resource_tracker.track(log=request):
        Step.from_cmdline(args)
