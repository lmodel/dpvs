---
search:
  boost: 10.0
---

# Class: External 


_Information about external characteristics that can be observed_



<div data-search-exclude markdown="1">



URI: [pd:External](https://w3id.org/lmodel/dpv/pd/External)





```mermaid
 classDiagram
    class External
    click External href "../External/"
      External <|-- Behavioural
        click Behavioural href "../Behavioural/"
      External <|-- Citizenship
        click Citizenship href "../Citizenship/"
      External <|-- Demographic
        click Demographic href "../Demographic/"
      External <|-- Ethnicity
        click Ethnicity href "../Ethnicity/"
      External <|-- Identifying
        click Identifying href "../Identifying/"
      External <|-- Language
        click Language href "../Language/"
      External <|-- MedicalHealth
        click MedicalHealth href "../MedicalHealth/"
      External <|-- Nationality
        click Nationality href "../Nationality/"
      External <|-- PersonalDocuments
        click PersonalDocuments href "../PersonalDocuments/"
      External <|-- PhysicalCharacteristic
        click PhysicalCharacteristic href "../PhysicalCharacteristic/"
      External <|-- Sexual
        click Sexual href "../Sexual/"
      External <|-- Vehicle
        click Vehicle href "../Vehicle/"
      
      
```





## Inheritance
* **External**
    * [Behavioural](Behavioural.md)
    * [Citizenship](Citizenship.md)
    * [Demographic](Demographic.md)
    * [Ethnicity](Ethnicity.md)
    * [Identifying](Identifying.md)
    * [Language](Language.md)
    * [Nationality](Nationality.md)
    * [PersonalDocuments](PersonalDocuments.md)
    * [PhysicalCharacteristic](PhysicalCharacteristic.md)
    * [Vehicle](Vehicle.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:External](https://w3id.org/lmodel/dpv/pd/External) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* External




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#External |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:External |
| native | pd:External |
| exact | dpv_pd:External, dpv_pd_owl:External |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: External
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#External
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about external characteristics that can be observed
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- External
exact_mappings:
- dpv_pd:External
- dpv_pd_owl:External
class_uri: pd:External

```
</details>

### Induced

<details>
```yaml
name: External
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#External
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about external characteristics that can be observed
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- External
exact_mappings:
- dpv_pd:External
- dpv_pd_owl:External
class_uri: pd:External

```
</details></div>