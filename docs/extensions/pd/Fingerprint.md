---
search:
  boost: 10.0
---

# Class: Fingerprint 


_Information about fingerprint used for biometric purposes_



<div data-search-exclude markdown="1">



URI: [pd:Fingerprint](https://w3id.org/lmodel/dpv/pd/Fingerprint)





```mermaid
 classDiagram
    class Fingerprint
    click Fingerprint href "../Fingerprint/"
      Biometric <|-- Fingerprint
        click Biometric href "../Biometric/"
      
      
```





## Inheritance
* [Biometric](Biometric.md) [ [Identifying](Identifying.md)]
    * **Fingerprint**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Fingerprint](https://w3id.org/lmodel/dpv/pd/Fingerprint) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Fingerprint




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Fingerprint |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Fingerprint |
| native | pd:Fingerprint |
| exact | dpv_pd:Fingerprint, dpv_pd_owl:Fingerprint |
| close | iso29100:PersonallyIdentifiableInformation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Fingerprint
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Fingerprint
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about fingerprint used for biometric purposes
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Fingerprint
exact_mappings:
- dpv_pd:Fingerprint
- dpv_pd_owl:Fingerprint
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: Biometric
class_uri: pd:Fingerprint

```
</details>

### Induced

<details>
```yaml
name: Fingerprint
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Fingerprint
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about fingerprint used for biometric purposes
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Fingerprint
exact_mappings:
- dpv_pd:Fingerprint
- dpv_pd_owl:Fingerprint
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: Biometric
class_uri: pd:Fingerprint

```
</details></div>