---
search:
  boost: 10.0
---

# Class: VehicalLicenseNumber 


_Information about vehicle license number_



<div data-search-exclude markdown="1">



URI: [pd:VehicalLicenseNumber](https://w3id.org/lmodel/dpv/pd/VehicalLicenseNumber)





```mermaid
 classDiagram
    class VehicalLicenseNumber
    click VehicalLicenseNumber href "../VehicalLicenseNumber/"
      VehicleLicense <|-- VehicalLicenseNumber
        click VehicleLicense href "../VehicleLicense/"
      
      
```





## Inheritance
* [External](External.md)
    * [Identifying](Identifying.md)
        * [VehicleLicense](VehicleLicense.md) [ [Vehicle](Vehicle.md)]
            * **VehicalLicenseNumber**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:VehicalLicenseNumber](https://w3id.org/lmodel/dpv/pd/VehicalLicenseNumber) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Vehicle License Number




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#VehicalLicenseNumber |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:VehicalLicenseNumber |
| native | pd:VehicalLicenseNumber |
| exact | dpv_pd:VehicalLicenseNumber, dpv_pd_owl:VehicalLicenseNumber |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VehicalLicenseNumber
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#VehicalLicenseNumber
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about vehicle license number
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Vehicle License Number
exact_mappings:
- dpv_pd:VehicalLicenseNumber
- dpv_pd_owl:VehicalLicenseNumber
is_a: VehicleLicense
class_uri: pd:VehicalLicenseNumber

```
</details>

### Induced

<details>
```yaml
name: VehicalLicenseNumber
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#VehicalLicenseNumber
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about vehicle license number
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Vehicle License Number
exact_mappings:
- dpv_pd:VehicalLicenseNumber
- dpv_pd_owl:VehicalLicenseNumber
is_a: VehicleLicense
class_uri: pd:VehicalLicenseNumber

```
</details></div>