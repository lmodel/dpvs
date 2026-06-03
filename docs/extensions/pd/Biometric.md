---
search:
  boost: 10.0
---

# Class: Biometric 


_Information about biometrics and biometric characteristics._



<div data-search-exclude markdown="1">



URI: [pd:Biometric](https://w3id.org/lmodel/dpv/pd/Biometric)





```mermaid
 classDiagram
    class Biometric
    click Biometric href "../Biometric/"
      Identifying <|-- Biometric
        click Identifying href "../Identifying/"
      

      Biometric <|-- FacialExpression
        click FacialExpression href "../FacialExpression/"
      Biometric <|-- FacialPrint
        click FacialPrint href "../FacialPrint/"
      Biometric <|-- Fingerprint
        click Fingerprint href "../Fingerprint/"
      Biometric <|-- Retina
        click Retina href "../Retina/"
      

      
```





## Inheritance
* **Biometric** [ [Identifying](Identifying.md)]
    * [FacialExpression](FacialExpression.md)
    * [FacialPrint](FacialPrint.md)
    * [Fingerprint](Fingerprint.md)
    * [Retina](Retina.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Biometric](https://w3id.org/lmodel/dpv/pd/Biometric) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Biometric




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Biometric |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Biometric |
| native | pd:Biometric |
| exact | dpv_pd:Biometric, dpv_pd_owl:Biometric |
| close | iso29100:PersonallyIdentifiableInformation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Biometric
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Biometric
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about biometrics and biometric characteristics.
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Biometric
exact_mappings:
- dpv_pd:Biometric
- dpv_pd_owl:Biometric
close_mappings:
- iso29100:PersonallyIdentifiableInformation
mixins:
- Identifying
class_uri: pd:Biometric

```
</details>

### Induced

<details>
```yaml
name: Biometric
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Biometric
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about biometrics and biometric characteristics.
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Biometric
exact_mappings:
- dpv_pd:Biometric
- dpv_pd_owl:Biometric
close_mappings:
- iso29100:PersonallyIdentifiableInformation
mixins:
- Identifying
class_uri: pd:Biometric

```
</details></div>