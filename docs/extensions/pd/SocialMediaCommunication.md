---
search:
  boost: 10.0
---

# Class: SocialMediaCommunication 


_Information about social media communication, including the_

_communication itself and metadata_



<div data-search-exclude markdown="1">



URI: [pd:SocialMediaCommunication](https://w3id.org/lmodel/dpv/pd/SocialMediaCommunication)





```mermaid
 classDiagram
    class SocialMediaCommunication
    click SocialMediaCommunication href "../SocialMediaCommunication/"
      Communication <|-- SocialMediaCommunication
        click Communication href "../Communication/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Communication](Communication.md)
        * **SocialMediaCommunication**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:SocialMediaCommunication](https://w3id.org/lmodel/dpv/pd/SocialMediaCommunication) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Social Media Communication




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#SocialMediaCommunication |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:SocialMediaCommunication |
| native | pd:SocialMediaCommunication |
| exact | dpv_pd:SocialMediaCommunication, dpv_pd_owl:SocialMediaCommunication |
| related | svd:Social |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SocialMediaCommunication
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SocialMediaCommunication
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about social media communication, including the

  communication itself and metadata'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Social Media Communication
exact_mappings:
- dpv_pd:SocialMediaCommunication
- dpv_pd_owl:SocialMediaCommunication
related_mappings:
- svd:Social
is_a: Communication
class_uri: pd:SocialMediaCommunication

```
</details>

### Induced

<details>
```yaml
name: SocialMediaCommunication
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SocialMediaCommunication
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about social media communication, including the

  communication itself and metadata'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Social Media Communication
exact_mappings:
- dpv_pd:SocialMediaCommunication
- dpv_pd_owl:SocialMediaCommunication
related_mappings:
- svd:Social
is_a: Communication
class_uri: pd:SocialMediaCommunication

```
</details></div>