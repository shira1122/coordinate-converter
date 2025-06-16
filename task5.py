def dd_to_dms(dd_list):
  """
 Converts coordinates from decimal (DD) format to degrees/minutes/seconds (DMS) format.
dd_list: a list of [longitude, latitude, (optional) height]
Returns: a list of [longitude_DMS, latitude_DMS, (if any) height]
  """

  def convert(dd, is_latitude):
      """
An internal function that performs the conversion of a single DD number to DMS.
      """
  #The direction representation on the map converts the value according to the positive/negative sign.
      if is_latitude:
          direction = 'N' if dd >= 0 else 'S'
      else:
          direction = 'E' if dd >= 0 else 'W'
#Calculation of the conversion
      dd = abs(dd)
      degrees = int(dd)
      minutes_float = (dd - degrees) * 60
      minutes = int(minutes_float)
      seconds = round((minutes_float - minutes) * 60, 2)

      return [degrees, minutes, seconds, direction]

#If height above water level is specified
  height = dd_list[2] if len(dd_list) > 2 else None

  # Convert length and width from sender to function
  lon_dms = convert(dd_list[0], is_latitude=False)
  lat_dms = convert(dd_list[1], is_latitude=True)

  if height is not None:
      return [lon_dms, lat_dms, height]
  else:
      return [lon_dms, lat_dms]


