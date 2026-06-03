---
search:
  boost: 10.0
---

# Class: BrowserFingerprint 


_Information about the web browser which is used as a 'fingerprint'_



<div data-search-exclude markdown="1">



URI: [pd:BrowserFingerprint](https://w3id.org/lmodel/dpv/pd/BrowserFingerprint)





```mermaid
 classDiagram
    class BrowserFingerprint
    click BrowserFingerprint href "../BrowserFingerprint/"
      DeviceBased <|-- BrowserFingerprint
        click DeviceBased href "../DeviceBased/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [DeviceBased](DeviceBased.md)
        * **BrowserFingerprint**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:BrowserFingerprint](https://w3id.org/lmodel/dpv/pd/BrowserFingerprint) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Browser Fingerprint




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#BrowserFingerprint |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:BrowserFingerprint |
| native | pd:BrowserFingerprint |
| exact | dpv_pd:BrowserFingerprint, dpv_pd_owl:BrowserFingerprint |
| close | iso29100:PersonallyIdentifiableInformation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BrowserFingerprint
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#BrowserFingerprint
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about the web browser which is used as a 'fingerprint'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Browser Fingerprint
exact_mappings:
- dpv_pd:BrowserFingerprint
- dpv_pd_owl:BrowserFingerprint
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: DeviceBased
class_uri: pd:BrowserFingerprint

```
</details>

### Induced

<details>
```yaml
name: BrowserFingerprint
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#BrowserFingerprint
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about the web browser which is used as a 'fingerprint'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Browser Fingerprint
exact_mappings:
- dpv_pd:BrowserFingerprint
- dpv_pd_owl:BrowserFingerprint
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: DeviceBased
class_uri: pd:BrowserFingerprint

```
</details></div>