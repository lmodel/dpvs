---
search:
  boost: 10.0
---

# Class: Tracking 


_Information used to track an individual or group e.g. location or email_



<div data-search-exclude markdown="1">



URI: [pd:Tracking](https://w3id.org/lmodel/dpv/pd/Tracking)





```mermaid
 classDiagram
    class Tracking
    click Tracking href "../Tracking/"
      Tracking <|-- Contact
        click Contact href "../Contact/"
      Tracking <|-- DeviceBased
        click DeviceBased href "../DeviceBased/"
      Tracking <|-- DigitalFingerprint
        click DigitalFingerprint href "../DigitalFingerprint/"
      Tracking <|-- DpvIdentifier
        click DpvIdentifier href "../DpvIdentifier/"
      Tracking <|-- DpvLocation
        click DpvLocation href "../DpvLocation/"
      Tracking <|-- UserAgent
        click UserAgent href "../UserAgent/"
      
      
```





## Inheritance
* **Tracking**
    * [Contact](Contact.md)
    * [DeviceBased](DeviceBased.md)
    * [DigitalFingerprint](DigitalFingerprint.md)
    * [DpvIdentifier](DpvIdentifier.md)
    * [DpvLocation](DpvLocation.md)
    * [UserAgent](UserAgent.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Tracking](https://w3id.org/lmodel/dpv/pd/Tracking) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Tracking




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Tracking |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Tracking |
| native | pd:Tracking |
| exact | dpv_pd:Tracking, dpv_pd_owl:Tracking |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Tracking
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Tracking
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information used to track an individual or group e.g. location or email
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Tracking
exact_mappings:
- dpv_pd:Tracking
- dpv_pd_owl:Tracking
class_uri: pd:Tracking

```
</details>

### Induced

<details>
```yaml
name: Tracking
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Tracking
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information used to track an individual or group e.g. location or email
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Tracking
exact_mappings:
- dpv_pd:Tracking
- dpv_pd_owl:Tracking
class_uri: pd:Tracking

```
</details></div>