---
search:
  boost: 10.0
---

# Class: VehicleLicense 


_Information about vehicle license_



<div data-search-exclude markdown="1">



URI: [pd:VehicleLicense](https://w3id.org/lmodel/dpv/pd/VehicleLicense)





```mermaid
 classDiagram
    class VehicleLicense
    click VehicleLicense href "../VehicleLicense/"
      Vehicle <|-- VehicleLicense
        click Vehicle href "../Vehicle/"
      Identifying <|-- VehicleLicense
        click Identifying href "../Identifying/"
      

      VehicleLicense <|-- VehicalLicenseNumber
        click VehicalLicenseNumber href "../VehicalLicenseNumber/"
      VehicleLicense <|-- VehicalLicenseRegistration
        click VehicalLicenseRegistration href "../VehicalLicenseRegistration/"
      

      
```





## Inheritance
* [External](External.md)
    * [Identifying](Identifying.md)
        * **VehicleLicense** [ [Vehicle](Vehicle.md)]
            * [VehicalLicenseNumber](VehicalLicenseNumber.md)
            * [VehicalLicenseRegistration](VehicalLicenseRegistration.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:VehicleLicense](https://w3id.org/lmodel/dpv/pd/VehicleLicense) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Vehicle License




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#VehicleLicense |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:VehicleLicense |
| native | pd:VehicleLicense |
| exact | dpv_pd:VehicleLicense, dpv_pd_owl:VehicleLicense |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VehicleLicense
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#VehicleLicense
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about vehicle license
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Vehicle License
exact_mappings:
- dpv_pd:VehicleLicense
- dpv_pd_owl:VehicleLicense
is_a: Identifying
mixins:
- Vehicle
class_uri: pd:VehicleLicense

```
</details>

### Induced

<details>
```yaml
name: VehicleLicense
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#VehicleLicense
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about vehicle license
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Vehicle License
exact_mappings:
- dpv_pd:VehicleLicense
- dpv_pd_owl:VehicleLicense
is_a: Identifying
mixins:
- Vehicle
class_uri: pd:VehicleLicense

```
</details></div>