---
search:
  boost: 10.0
---

# Class: DigitalFingerprint 


_Information about a 'digital fingerprint' created for identification_



<div data-search-exclude markdown="1">



URI: [pd:DigitalFingerprint](https://w3id.org/lmodel/dpv/pd/DigitalFingerprint)





```mermaid
 classDiagram
    class DigitalFingerprint
    click DigitalFingerprint href "../DigitalFingerprint/"
      Tracking <|-- DigitalFingerprint
        click Tracking href "../Tracking/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * **DigitalFingerprint**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:DigitalFingerprint](https://w3id.org/lmodel/dpv/pd/DigitalFingerprint) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Digital Fingerprint




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#DigitalFingerprint |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:DigitalFingerprint |
| native | pd:DigitalFingerprint |
| exact | dpv_pd:DigitalFingerprint, dpv_pd_owl:DigitalFingerprint |
| close | iso29100:PersonallyIdentifiableInformation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DigitalFingerprint
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#DigitalFingerprint
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about a 'digital fingerprint' created for identification
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Digital Fingerprint
exact_mappings:
- dpv_pd:DigitalFingerprint
- dpv_pd_owl:DigitalFingerprint
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: Tracking
class_uri: pd:DigitalFingerprint

```
</details>

### Induced

<details>
```yaml
name: DigitalFingerprint
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#DigitalFingerprint
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about a 'digital fingerprint' created for identification
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Digital Fingerprint
exact_mappings:
- dpv_pd:DigitalFingerprint
- dpv_pd_owl:DigitalFingerprint
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: Tracking
class_uri: pd:DigitalFingerprint

```
</details></div>