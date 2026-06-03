---
search:
  boost: 10.0
---

# Class: VehicalLicenseRegistration 


_Information about vehicle license registration_



<div data-search-exclude markdown="1">



URI: [pd:VehicalLicenseRegistration](https://w3id.org/lmodel/dpv/pd/VehicalLicenseRegistration)





```mermaid
 classDiagram
    class VehicalLicenseRegistration
    click VehicalLicenseRegistration href "../VehicalLicenseRegistration/"
      VehicleLicense <|-- VehicalLicenseRegistration
        click VehicleLicense href "../VehicleLicense/"
      
      
```





## Inheritance
* [External](External.md)
    * [Identifying](Identifying.md)
        * [VehicleLicense](VehicleLicense.md) [ [Vehicle](Vehicle.md)]
            * **VehicalLicenseRegistration**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:VehicalLicenseRegistration](https://w3id.org/lmodel/dpv/pd/VehicalLicenseRegistration) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Vehicle License Registration




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#VehicalLicenseRegistration |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:VehicalLicenseRegistration |
| native | pd:VehicalLicenseRegistration |
| exact | dpv_pd:VehicalLicenseRegistration, dpv_pd_owl:VehicalLicenseRegistration |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VehicalLicenseRegistration
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#VehicalLicenseRegistration
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about vehicle license registration
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Vehicle License Registration
exact_mappings:
- dpv_pd:VehicalLicenseRegistration
- dpv_pd_owl:VehicalLicenseRegistration
is_a: VehicleLicense
class_uri: pd:VehicalLicenseRegistration

```
</details>

### Induced

<details>
```yaml
name: VehicalLicenseRegistration
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#VehicalLicenseRegistration
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about vehicle license registration
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Vehicle License Registration
exact_mappings:
- dpv_pd:VehicalLicenseRegistration
- dpv_pd_owl:VehicalLicenseRegistration
is_a: VehicleLicense
class_uri: pd:VehicalLicenseRegistration

```
</details></div>